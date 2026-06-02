# 🏢 Unit Management System

The **Unit Management System** is a robust solution designed to streamline the administration, tracking, and organization of organizational units, assets, and soldier records. This repository contains the core logic, API architecture, and interfaces for managing these units efficiently.

---

## 📊 System Endpoints & API

The following table summarizes the system's endpoints as defined in `Unit managment endpoints.xlsx`:

| Operation | Method | Path | Input | Output | Response Codes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Get All Soldiers** | `GET` | `/soldiers` | *None* | All soldiers: list | 200 / 500 |
| **Get Soldier Details** | `GET` | `/soldiers/{id}` | `soldier_id` | Soldier: dict / None | 200 / 404 |
| **Create New Soldier** | `POST` | `/soldiers` | `data` | id -> system msg | 201 / 500 |
| **Update Soldier** | `PUT` | `/soldiers/{id}` | `soldier_id`, `data` | id -> system msg | 200 / 404 |
| **Delete Soldier** | `DELETE` | `/soldiers/{id}` | `soldier_id` | id -> system msg | 200 / 404 |

---

## 🗄️ 1. Data Modeling

The system's data model was built using a hierarchical and modular approach, recognizing that an organization consists of nested sub-units, specific resources, and personnel:
* **Unit:** The top-level entity in the system. It contains a unique identifier, unit name, and its hierarchical relations (e.g., Brigade -> Battalion -> Company).
* **Soldier:** An entity representing the personnel assigned to a unit. The model includes fields such as full name, rank, role, availability status, and a foreign key (`unit_id`) that links them to their respective organic unit.
* **Relationships:** The database architecture utilizes a **One-to-Many** relationship (one unit can contain multiple soldiers). This structure allows for rapid filtering and real-time retrieval of all personnel associated with any specific unit.

---

## 🆔 2. Soldier ID Management

Soldier identifiers within the system are managed under strict validation and data integrity protocols:
* **Uniqueness:** Each soldier is assigned a unique identifier (`soldier_id`) that serves as the Primary Key. The system strictly restricts and prevents any duplicate IDs.
* **Validation:** When creating a new soldier (`POST /soldiers`) or updating existing records (`PUT /soldiers/{id}`), validation logic runs to ensure the ID complies with the required formatting standards (e.g., correct character length, numeric values only).
* **State Management:** Accessing a specific soldier for data retrieval, updates, or deletion is performed securely and directly through the URL using their unique ID (as demonstrated by the `/soldiers/{id}` paths).

---

## 🧩 3. Challenges & Solutions

During the development process, several critical technical challenges were addressed:
* **Referential Integrity on Deletions:** Deleting a soldier or a unit could potentially cause orphan records or break data consistency.
  * *Solution:* We implemented safety guardrails that prevent the deletion of entities with active system dependencies, accompanied by standard error responses (`404` or `500`) if the resource is missing or the action fails.
* **Edge-Case Error Handling:** Ensuring server stability when receiving malformed, incomplete, or invalid payloads from the client.
  * *Solution:* Global error-handling middleware was integrated to catch exceptions gracefully. Instead of crashing, the system returns structured responses (`id -> system msg`) alongside standard HTTP status codes (`404` for Not Found, `500` for Internal Server Error).

---

## 💻 4. Getting Started & Installation

Follow these steps to install the required external dependencies and run the project locally on your machine.

### Prerequisites
Ensure you have the required environment installed (e.g., Node.js or Python, depending on your project's backend stack).

### Step-by-Step Guide:

1. **Clone the Repository:**
```bash
   git clone [https://github.com/hallelkedar/Unit_managment_system.git](https://github.com/hallelkedar/Unit_managment_system.git)
   cd Unit_managment_system
