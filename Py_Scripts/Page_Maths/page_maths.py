import math

def calculate_pages(total_boxes, boxes_per_page):
    full_pages = total_boxes // boxes_per_page
    remaining_boxes = total_boxes % boxes_per_page
    
    if remaining_boxes > 0:
        return full_pages + 1, full_pages, remaining_boxes
    else:
        return full_pages, full_pages, 0

def main():
    try:
        total_boxes = int(input("Enter the total number of boxes: "))
        boxes_per_page = int(input("Enter the number of boxes per page: "))
        
        if total_boxes < 0 or boxes_per_page <= 0:
            raise ValueError("The number of boxes and boxes per page must be positive numbers.")
        
        pages_needed, full_pages_count, remaining_boxes = calculate_pages(total_boxes, boxes_per_page)
        
        print(f"Total number of boxes: {total_boxes}")
        print(f"Number of boxes per page: {boxes_per_page}")
        print(f"Total pages needed: {pages_needed}")
        print(f"Pages with {boxes_per_page} boxes: {full_pages_count}")
        
        if remaining_boxes > 0:
            print(f"One additional page with {remaining_boxes} box(es)")
        else:
            print("All pages are fully filled.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
