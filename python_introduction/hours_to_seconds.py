hour = 3600  # 1 hour = 60 minutes * 60 seconds
def hours_to_seconds(hours):
    """Convert hours to seconds."""
    return hours * hour

def main():
    hours = 2  # Example input
    seconds = hours_to_seconds(hours)
    print(f"{hours} hour(s) is {seconds} second.")
if __name__ == "__main__":
    main()
# This code converts hours to seconds, demonstrating a simple time conversion.