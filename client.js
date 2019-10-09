let grpc = require("grpc");
var protoLoader = require("@grpc/proto-loader");

const protoPaths = [
    "protos/Hello.proto"
]
//Load the protobuf
var proto = grpc.loadPackageDefinition(
    protoLoader.loadSync(protoPaths, {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    })
);

const REMOTE_SERVER = "0.0.0.0:5051";

//Create gRPC client
let client = new proto.demo.Hello(
    REMOTE_SERVER,
    grpc.credentials.createInsecure()
);


client.call({}, (error, response) => {
    // console.log("response===>", error, response)
    if (error) {
        console.error("This is error", error)
    }
    console.log("response===>", error, response)
}
);