base_url ?=https://computer-database.gatling.io
parallel ?= 3
SELENIUM_HOST ?= 172.17.0.1
SELENIUM_PORT ?= 4444
SELENOID_UI_PORT ?= 8080
run ?= test

export base_url
export parallel
export SELENIUM_HOST
export SELENIUM_PORT
export SELENOID_UI_PORT
export run

test: clean
	docker pull selenoid/vnc_chrome:91.0
	docker-compose build
	docker-compose up

.PHONY: report
report:
	open report/dashboard.html

clean:
	@echo "+-+-+-+-+-+-+-+-+"
	@echo "|C|L|E|A|N|I|N|G|"
	@echo "+-+-+-+-+-+-+-+-+"
	docker-compose -f docker-compose.yml down
	docker rmi -f computer-database-ui-tests
	rm -rf report
	@echo "+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+"
	@echo "|C|L|E|A|N|I|N|G| |F|I|N|I|S|H|E|D|"
	@echo "+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+"

prune: clean
	@echo
	@echo "+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+"
	@echo "|R|E|M|O|V|I|N|G| |D|O|C|K|E|R| |I|M|A|G|E|S|"
	@echo "+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+"
	docker-compose down --rmi all
	docker rmi -f selenoid/vnc_chrome:91.0
	@echo "+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+"
	@echo "|A|L|L| |R|E|L|A|T|E|D| |I|M|A|G|E|S| |R|E|M|O|V|E|D|"
	@echo "+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+"
