from app import seed_order_history

if __name__ == '__main__':
    # will attach to the first user found in the DB if no user_id is provided
    inserted = seed_order_history()
    print(f'Inserted {inserted} order history records.')
