def process_test_data(test_csv_path, output_csv_path, model, image_dir):
    test_df = pd.read_csv(test_csv_path)
    predictions = []
    
    for _, row in test_df.iterrows():
        image_path = os.path.join(image_dir, f'{row["index"]}.jpg')
        entity_type = predict_entity(image_path, model)
        entity_value = extract_entity_value(image_path, entity_type)
        
        predictions.append({
            'index': row['index'],
            'prediction': entity_value
        })
    
    # Save the predictions to CSV
    predictions_df = pd.DataFrame(predictions)
    predictions_df.to_csv(output_csv_path, index=False)
