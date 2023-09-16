class Complaint:
    def __init__(self, category, description):
        self.category = category
        self.description = description
        self.status = "Pending"

class ComplaintManagementSystem:
    def __init__(self):
        self.complaints = []

    def submit_complaint(self, category, description):
        complaint = Complaint(category, description)
        self.complaints.append(complaint)
        return "Complaint submitted successfully!"

    def view_complaints(self):
        if not self.complaints:
            return "No complaints available."
        
        complaint_list = "\n".join(f"Category: {complaint.category}\nDescription: {complaint.description}\nStatus: {complaint.status}\n" for complaint in self.complaints)
        return complaint_list

    def update_complaint_status(self, complaint_index, status):
        if 0 <= complaint_index < len(self.complaints):
            self.complaints[complaint_index].status = status
            return "Complaint status updated successfully!"
        return "Invalid complaint index."

# Creating an instance of the Complaint Management System
cms = ComplaintManagementSystem()

while True:
    print("\nComplaint Management System")
    print("1. Submit Complaint")
    print("2. View Complaints")
    print("3. Update Complaint Status")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter complaint category: ")
        description = input("Enter complaint description: ")
        result = cms.submit_complaint(category, description)
        print(result)

    elif choice == "2":
        complaint_list = cms.view_complaints()
        print("Complaints:\n", complaint_list)

    elif choice == "3":
        complaint_index = int(input("Enter complaint index: "))
        status = input("Enter new status: ")
        result = cms.update_complaint_status(complaint_index, status)
        print(result)

    elif choice == "4":
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
