-- This script implements MYSQL trigger
CREATE TRIGGER buy_buy_buy
BEFORE INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
