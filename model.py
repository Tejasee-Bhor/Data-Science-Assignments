{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "138e2d0e-dd2a-4508-9939-d36a18265057",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\dell\\anaconda3\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\dell\\anaconda3\\lib\\site-packages (1.5.2)\n",
      "Requirement already satisfied: joblib in c:\\users\\dell\\anaconda3\\lib\\site-packages (1.4.2)\n",
      "Requirement already satisfied: streamlit in c:\\users\\dell\\anaconda3\\lib\\site-packages (1.32.0)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: scipy>=1.6.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from scikit-learn) (1.13.1)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from scikit-learn) (3.5.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (23.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (10.3.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (2.32.2)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (4.11.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\dell\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\dell\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.7.4)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas scikit-learn joblib streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "077df666-b631-45ba-b258-54fc7565e918",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['model.pkl']"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# model.py\n",
    "\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "import joblib\n",
    "\n",
    "# Load the Titanic dataset\n",
    "data = pd.read_csv('Titanic_train.csv')\n",
    "\n",
    "# Data Preprocessing\n",
    "data['Age'].fillna(data['Age'].mean(), inplace=True)\n",
    "data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)\n",
    "\n",
    "# Drop non-numeric columns that are not needed for the model\n",
    "data.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True)\n",
    "\n",
    "# Convert categorical variables into dummy/indicator variables\n",
    "data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)\n",
    "\n",
    "# Split data into features (X) and target (y)\n",
    "X = data.drop(columns=['Survived'])\n",
    "y = data['Survived']\n",
    "\n",
    "# Split dataset into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Train the logistic regression model\n",
    "model = LogisticRegression(max_iter=200)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Save the model to a file\n",
    "joblib.dump(model, 'model.pkl')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96673cec-c8c2-4cea-85df-c33a0c636cb2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
