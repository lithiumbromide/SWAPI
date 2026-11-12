---
title: "Login Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "Login"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Login.html"
---

# Login Method (IPDMWConnection)

Logs the user into SOLIDWORKS Workgroup PDM and is required to initialize the [IPDMWConnection](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html) object for subsequent method calls.

## Syntax

### Visual Basic (Declaration)

```vb
Function Login( _
   ByVal user As System.String, _
   ByVal password As System.String, _
   ByVal server As System.String, _
   Optional ByVal request_port As System.Integer, _
   Optional ByVal data_port As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim user As System.String
Dim password As System.String
Dim server As System.String
Dim request_port As System.Integer
Dim data_port As System.Integer
Dim value As System.Integer

value = instance.Login(user, password, server, request_port, data_port)
```

### C#

```csharp
System.int Login(
   System.string user,
   System.string password,
   System.string server,
   System.int request_port,
   System.int data_port
)
```

### C++/CLI

```cpp
System.int Login(
   System.String^ user,
   System.String^ password,
   System.String^ server,
   System.int request_port,
   System.int data_port
)
```

### Parameters

- `user`: Name of user in SOLIDWORKS Workgroup PDM
- `password`: Password of user in SOLIDWORKS Workgroup PDM
- `server`: Name of the server (DNS name or IP address)
- `request_port`: Request port number; defaults to 40000
- `data_port`: Data port number; defaults to 30000

### Return Value

0 if successful, non-0 if not

## VBA Syntax

See [PDMWConnection::Login](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~Login.html).

## Examples

[Extract Embedded eDrawings Data (VBA)](Extract_Embedded_eDrawings_Data_Example_VB.htm)
[Get Specific Document (VBA)](Get_Specific_Document_Example_VB.htm)
[List Assemblies Where Part Used (VBA)](List_Assemblies_Where_Part_Used_Example_VB.htm)
[Get Names of Projects for All Documents in Vault (VB.NET)](Get_Names_Projects_for_Documents_in_Vault_Example_VBNET.htm)

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWConnection::Logout Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Logout.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
