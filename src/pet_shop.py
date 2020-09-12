# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(dict):
    name = dict["name"]
    return name


def get_total_cash(dict):
    total_cash = dict["admin"]["total_cash"]
    return total_cash


def add_or_remove_cash(dict, cash_difference):
    dict["admin"]["total_cash"] += cash_difference
    return dict["admin"]["total_cash"]


def get_pets_sold(dict):
    no_pets_sold = dict["admin"]["pets_sold"]
    return no_pets_sold


def increase_pets_sold(dict, num_of_pets_change):
    dict["admin"]["pets_sold"] += num_of_pets_change
    return dict["admin"]["pets_sold"]


def get_stock_count(pets_dict):
    stock_count = len(pets_dict["pets"])
    return stock_count    