install-pre-commit-deps-mac:
	brew install pre-commit terraform-docs tfsec checkov terrascan tfupdate
	pre-commit install

install-pre-commit-deps-linux:
	sudo apt update
	sudo apt install -y unzip software-properties-common python3 python3-pip python-is-python3
	python3 -m pip install --upgrade pip
	pip3 install --no-cache-dir pre-commit
	curl -L "$(curl -s https://api.github.com/repos/terraform-docs/terraform-docs/releases/latest | grep -o -E -m 1 "https://.+?-linux-amd64.tar.gz")" > terraform-docs.tgz && tar -xzf terraform-docs.tgz terraform-docs && rm terraform-docs.tgz && chmod +x terraform-docs && sudo mv terraform-docs /usr/bin/
	curl -L "$(curl -s https://api.github.com/repos/minamijoyo/tfupdate/releases/latest | grep -o -E -m 1 "https://.+?_linux_amd64.tar.gz")" > tfupdate.tar.gz && tar -xzf tfupdate.tar.gz tfupdate && rm tfupdate.tar.gz && sudo mv tfupdate /usr/bin/
	curl -L "$(curl -s https://api.github.com/repos/tenable/terrascan/releases/latest | grep -o -E -m 1 "https://.+?_Linux_x86_64.tar.gz")" > terrascan.tar.gz && tar -xzf terrascan.tar.gz terrascan && rm terrascan.tar.gz && sudo mv terrascan /usr/bin/ && terrascan init

install-pre-commit-mac: install-pre-commit-deps-mac
	pre-commit install

install-pre-commit-linux: install-pre-commit-deps-linux
	pre-commit install

build:
	docker compose build mage_ingester_production spark spark-worker

ingest_data:
	docker compose run --rm mage_ingester_production mage run mage meteorite_landings
	docker compose down

ui:
	docker compose up mage_ui
