#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
セキュリティチェックシートをMarkdownからCSVに変換するスクリプト
"""

import csv
import re

def parse_checksheet_md(file_path):
    checksheet_data = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    lines = content.strip().split('\n')
    
    for line in lines:
        if line.startswith('|') and line.endswith('|'):
            if '重要性' in line or '----' in line:
                continue
            
            columns = [col.strip() for col in line.split('|')[1:-1]]
            
            if len(columns) >= 4:
                no = columns[0]
                importance = columns[1]
                category = columns[2]
                question = columns[3]
                
                importance_clean = importance.replace('🟥 高', '高').replace('🟧 中', '中').replace('🟩 低', '低')
                
                checksheet_data.append({
                    'No': no,
                    '重要性': importance_clean,
                    '項目': category,
                    '依頼資料・質問': question
                })
    
    return checksheet_data

def write_csv(data, output_file):
    """データをCSVファイルに書き込み"""
    if not data:
        print("変換するデータが見つかりませんでした。")
        return
    
    fieldnames = ['No', '重要性', '項目', '依頼資料・質問']
    
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"CSVファイル '{output_file}' が正常に作成されました。")
    print(f"変換された項目数: {len(data)}")

def main():
    """メイン処理"""
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    input_file = os.path.join(project_root, 'checksheet.md')
    output_file = os.path.join(project_root, 'checksheet.csv')
    
    try:
        print(f"Markdownファイルを解析中: {os.path.basename(input_file)}")
        data = parse_checksheet_md(input_file)
        
        if data:
            print(f"CSVファイルに変換中: {os.path.basename(output_file)}")
            write_csv(data, output_file)
        else:
            print("データの解析に失敗しました。")
            
    except FileNotFoundError:
        print(f"エラー: '{os.path.basename(input_file)}' が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main() 