import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # print(data)
    # Extract the relevant data
    jobs = data['data']
    extracted_data = []
    for job in jobs:
        extracted_data.append({
            'role_id': job['id'],
            'role_name': job['title'],
            'role_url': job['url'],
            'company_name': job['company']['name'],
            'location': job.get('location', ''),
            'type': job.get('type', ''),
            'post_date': job.get('postDate', ''),
            'benefits': job.get('benefits', '')
        })

    # Create a pandas DataFrame
    df = pd.DataFrame(extracted_data)
    
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
