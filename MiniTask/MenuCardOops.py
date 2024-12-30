class MenuCard:
    def __init__(self):
        self.menu_card = ['Dosa', 'Idly', 'Biriyani']

    def display(self):
        if self.menu_card:
            print("\nCurrent Menu:")
            for item in self.menu_card:
                print(item)
        else:
            print("\nThe menu is currently empty.")

    def add(self, value):
        self.menu_card.append(value)
        print(f'\n"{value}" added successfully.')
        self.display()

    def update(self, pre_value, update_value):
        if pre_value in self.menu_card:
            index = self.menu_card.index(pre_value)
            self.menu_card[index] = update_value
            print(f'\n"{pre_value}" updated to "{update_value}" successfully.')
            self.display()
        else:
            print(f'\n"{pre_value}" not found in the menu. Please enter a valid item to update.')

    def delete(self, value):
        if value in self.menu_card:
            self.menu_card.remove(value)
            print(f'\n"{value}" deleted successfully.')
            self.display()
        else:
            print(f'\n"{value}" not found in the menu. Please enter a valid item to delete.')


def main():
    menu_card_object = MenuCard()

    while True:
        print('\nSelect an option:')
        print('1. Display Menu')
        print('2. Add Dish')
        print('3. Update Dish')
        print('4. Delete Dish')
        print('5. Exit')

        choice = int(input('Enter your choice: '))
        if choice == 1:
            menu_card_object.display()
        elif choice == 2:
            value = input('Enter the dish you want to add: ')
            menu_card_object.add(value)
        elif choice == 3:
            menu_card_object.display()
            pre_value = input('Enter the dish you want to update: ')
            update_value = input('Enter the new dish to replace it: ')
            menu_card_object.update(pre_value, update_value)
        elif choice == 4:
            menu_card_object.display()
            delete_value = input('Enter the dish you want to delete: ')
            menu_card_object.delete(delete_value)
        elif choice == 5:
            print('Exiting... Goodbye!')
            break
        else:
            print('Invalid choice. Please select a valid option.')

if __name__ == '__main__':
    main()
