# Retail AI Assistant (Agentic AI System)

## Overview

This project implements a Retail AI Assistant that simulates two business roles:

1. **Personal Shopper (Revenue Agent)**

   * Recommends products based on customer preferences.
   * Considers budget, size availability, stock levels, sale status, tags, and bestseller score.

2. **Customer Support Assistant (Operations Agent)**

   * Retrieves order details.
   * Evaluates return eligibility based on store policies.
   * Explains return decisions clearly and accurately.

The system is built using **LangChain**, **Google Gemini**, and structured tool calling to ensure accurate and reliable responses.

---

## Features

### Personal Shopper

* Product discovery using natural language
* Multi-constraint reasoning
* Budget-aware recommendations
* Stock availability verification
* Sale and clearance prioritization
* Bestseller ranking consideration
* Explanation of recommendation reasoning

### Customer Support

* Order lookup
* Product lookup
* Return eligibility evaluation
* Policy-based reasoning
* Error handling for invalid orders/products

### Agent Capabilities

* Dynamic tool selection
* Function calling
* Reduced hallucinations
* Structured reasoning
* CLI-based interaction

---

## Project Structure

```text
Agentic-Shopper/
│
├── agent/
│   ├── __init__.py
│   ├── prompts.py
│   └── shopping_agent.py
│
├── tools/
│   ├── __init__.py
│   ├── product_tools.py
│   ├── order_tools.py
│   └── return_tools.py
│
├── data/
│   ├── product_inventory.csv
│   ├── orders.csv
│   └── policy.txt
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Dataset

### Product Inventory

Fields:

* product_id
* title
* vendor
* price
* compare_at_price
* tags
* sizes_available
* stock_per_size
* is_sale
* is_clearance
* bestseller_score

### Orders

Fields:

* order_id
* order_date
* product_id
* size
* price_paid
* customer_id

### Policy File

Contains:

* Normal return window
* Sale item return rules
* Clearance rules
* Vendor-specific exceptions
* Exchange rules

---

## Tools

The agent uses four structured tools.

### search_products()

Searches inventory using filters.

Parameters:

* max_price
* size
* is_sale
* tags

Returns:

* Matching products
* Sorted by bestseller score

---

### get_product()

Retrieves product information.

Parameters:

* product_id

Returns:

* Product details
* Error if product does not exist

---

### get_order()

Retrieves order information.

Parameters:

* order_id

Returns:

* Order details
* Error if order does not exist

---

### evaluate_return()

Evaluates return eligibility.

Parameters:

* order_id

Returns:

* Return decision
* Explanation of policy application

---

## Agent Architecture

### Why This Structure?

The project separates:

1. Reasoning Layer (LLM)
2. Data Retrieval Layer (Tools)

The LLM is responsible for:

* Understanding user intent
* Selecting the appropriate tool
* Explaining decisions

The tools are responsible for:

* Retrieving factual information
* Applying business rules
* Preventing hallucinations

This separation improves reliability and maintainability.

---

## Hallucination Prevention

The system minimizes hallucinations by:

* Using tool-based retrieval
* Returning real inventory data
* Returning real order data
* Rejecting unknown product IDs
* Rejecting unknown order IDs
* Applying explicit return policies

The assistant never invents product or order information.

---

## Tool Selection Strategy

### Shopping Queries

Example:

```text
I need a modest evening gown under $300 in size 8.
```

Agent actions:

1. Extract constraints
2. Call search_products()
3. Filter by:

   * Price
   * Size availability
   * Stock
   * Tags
4. Rank by bestseller score
5. Explain recommendation

---

### Support Queries

Example:

```text
Can I return order O0009?
```

Agent actions:

1. Call get_order()
2. Call evaluate_return()
3. Apply policy rules
4. Return decision with explanation

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Agentic-Shopper
```

### Create Environment

```bash
conda create -n retail-ai python=3.11
conda activate retail-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## Running the Application

```bash
python main.py
```

Example:

```text
User:
I need a modest evening gown under $300 in size 8.

Assistant:
Based on your requirements, I recommend...
```

---

## Example Queries

### Shopping Scenario 1

```text
I need a modest evening gown under $300 in size 8.
```

### Shopping Scenario 2

```text
Show me the best sale dresses available in size 10.
```

### Support Scenario 1

```text
Can I return order O0009?
```

### Support Scenario 2

```text
Give me the details of product P0020.
```

### Edge Case

```text
Can I return order O9999?
```

Expected Response:

```text
Order not found.
```

---

## Technologies Used

* Python
* Pandas
* LangChain
* Google Gemini 2.5 Flash
* Pydantic
* dotenv

---

## Future Improvements

* Web UI using Streamlit
* Vector search for product discovery
* Conversation memory
* Recommendation scoring engine
* Advanced return policy engine
* Multi-agent architecture

---

## Author

Anant Pratap Singh

Agentic Retail AI Assistant Assignment
