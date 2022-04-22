-- This script creates a trigger to reset 'valid_email'
CREATE TRIGGER validate
BEFORE UPDATE ON users
FOR EACH ROW
SET valid_email = 0
IF NEW.email <> OLD.email;
