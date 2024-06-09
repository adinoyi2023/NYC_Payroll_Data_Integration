import psycopg2

def run_etl():
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_user",
        password="your_password"
    )
    cursor = conn.cursor()
    
    # Call the transformation functions
    cursor.execute("CALL transform_load_2020();")
    cursor.execute("CALL transform_load_2021();")
    
    # Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    run_etl()
