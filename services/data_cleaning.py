
def string_row_finder(df_row, text: list):
    """Find the index for rows based in regular expressions"""
    for txt in text:
        for idx in range(len(df_row)):
            if len(re.findall(rf"{txt}", df_row[idx], re.IGNORECASE)) != 0:
                rows_idx.append(idx)