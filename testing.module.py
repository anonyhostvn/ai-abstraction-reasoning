from read_data import InputMachine

# đọc tất cả các file trong folder training
train_data = InputMachine.read_test_input("training")
# Duyệt hết tất cả dữ liệu
for data in train_data:
    print(data.get("train"))
    print(data.get("test"))
    print(" ======== ")

# đọc tất cả các file trong folder test
test_data = InputMachine.read_test_input("test")

# đọc tất cả các file trong folder evaluation
evaluation_data = InputMachine.read_test_input("evaluation")