# Task Manager

[![CI Pipeline](https://github.com/CO0LGIRL/task-manager/actions/workflows/ci.yml/badge.svg)](https://github.com/CO0LGIRL/task-manager/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Kafka](https://img.shields.io/badge/Apache%20Kafka-latest-black)
![ClickHouse](https://img.shields.io/badge/ClickHouse-latest-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![License](https://img.shields.io/badge/License-MIT-important)

Масштабируемая микросервисная экосистема для управления задачами с выделенным аналитическим движком. Проект спроектирован с использованием принципов **EDA (Event-Driven Architecture)** и разделения операционных (OLTP) и аналитических (OLAP) данных.

---

## 🏗 Архитектура системы

Проект реализует паттерн распределенной системы, где сервисы взаимодействуют асинхронно:



* **api-service**: Основной сервис управления задачами. Использует PostgreSQL для транзакционных данных и выступает в роли **Kafka Producer**.
* **analytics-service**: Высокопроизводительный сервис аналитики. Работает как **Kafka Consumer**, агрегируя события в OLAP-хранилище ClickHouse.
* **common**: Общий модуль с контрактами данных (Pydantic), обеспечивающий согласованность (Event Schemas) между сервисами.

---

## 🎯 Основной функционал

* **Task Management:** Полный REST API для управления жизненным циклом задач.
* **Event-Driven:** Асинхронная передача событий через брокер сообщений Kafka.
* **OLAP Analytics:** Сбор и обработка метрик в ClickHouse для высокоскоростной агрегации.
* **Schema Validation:** Строгая типизация и валидация контрактов событий с помощью Pydantic.
* **CI/CD Ready:** Интегрированные GitHub Actions для линтинга (flake8) и тестирования.
* **Developer Experience:** Полная автоматизация локального развертывания через Makefile.

---

## 🛠 Технологический стек

* **Backend:** Python 3.10, Django 4.2, DRF
* **Message Broker:** Apache Kafka
* **Databases:** PostgreSQL 15, ClickHouse
* **Infrastructure:** Docker & Docker Compose
* **Testing & Quality:** PyTest, Unittest.mock, Flake8
* **CI/CD:** GitHub Actions

---

## 🚀 Быстрый старт

### Требования
* Docker & Docker Compose
* Make (опционально)

### Развертывание
```bash
make build
make up

make migrate

docker-compose ps