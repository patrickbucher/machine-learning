#!/usr/bin/env python

import pandas as pd


def main():
    df = pd.read_csv('movies_content.csv')
    print(df)


if __name__ == '__main__':
    main()
