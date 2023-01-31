const { Client } = import("@opensearch-project/opensearch");
const { defaultProvider } = import("@aws-sdk/credential-provider-node");
const createAwsOpensearchConnector = import("aws-opensearch-connector");

var host = 'https://search-meta-search-v4-6cloxdgo2wnscy6ohegxjkywwy.ca-central-1.es.amazonaws.com' // e.g. https://my-domain.region.es.amazonaws.com

const getClient = async () => {
    const awsCredentials = await defaultProvider()();
    const connector = createAwsOpensearchConnector({
        credentials: awsCredentials,
        region: process.env.AWS_REGION ?? 'ca-central-1',
        getCredentials: function(cb) {
            return cb();
        }
    });
    return new Client({
        ...connector,
        node: host,
    });
}

async function search() {

    // Initialize the client.
    var client = await getClient();

    // Create an index.
    var index_name = "test-index";
    var response = await client.indices.create({
        index: index_name,
    });

    console.log("Creating index:");
    console.log(response.body);

    // Add a document to the index.
    var document = {
        "title": "Moneyball",
        "director": "Bennett Miller",
        "year": "2011"
    };

    var response = await client.index({
        index: index_name,
        body: document
    });

    console.log(response.body);
}

export const handler = async(event) => {
    console.log("in");
// search().catch(console.log);
    return {
        statusCode: 200,
        body: JSON.stringify("retrun")
    }
}