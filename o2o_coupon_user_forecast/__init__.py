# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def convert_rate(row):
    if row.isna():
        return 1.0
    elif ':' in row:
        rows = row.split(':')
        return 1.0 - rows[1]/rows[0]
    return float(row)


def get_discount_type(row):
    pass


def get_discount_man(row):
    pass


def process_data(df):
    df['discount_rate'] = df['Discount_rate'].apply(convert_rate)
    return df


def main():
    # online_train_filename = 'files/ccf_offline_stage1_train.csv'
    # df_online_train = pd.read_csv(online_train_filename)

    offline_train_filename = 'files/ccf_online_stage1_train.csv'
    df_offline_train = pd.read_csv(offline_train_filename)

    # offline_test_filename = 'files/ccf_online_stage1_test_revised.csv'
    # df_offline_test = pd.read_csv(offline_test_filename)

    df_offline_train = process_data(df_offline_train)


if __name__ == '__main__':
    main()
