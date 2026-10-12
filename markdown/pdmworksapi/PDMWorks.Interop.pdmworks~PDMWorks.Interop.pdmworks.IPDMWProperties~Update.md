---
title: "Update Method (IPDMWProperties)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProperties"
member: "Update"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties~Update.html"
---

# Update Method (IPDMWProperties)

Updates SOLIDWORKS Workgroup PDM vault.

## Syntax

### Visual Basic (Declaration)

```vb
Function Update() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProperties
Dim value As System.Integer

value = instance.Update()
```

### C#

```csharp
System.int Update()
```

### C++/CLI

```cpp
System.int Update();
```

### Return Value

0 if successful, non-0 if not

## VBA Syntax

See [PDMWProperties::Update](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProperties~Update.html).

## Remarks

To update the SOLIDWORKS Workgroup PDM vault, use this method after using:

- [IPDMWProperties::Add](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties~Add.html) to add a new property.
- [IPDMWProperty::Value](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty~Value.html) to change an existing property.

If the Allow change document properties check box was not selected on the Vault Settings tab on the SOLIDWORKS Workgroup PDM VaultAdmin dialog box in the SOLIDWORKS Workgroup PDM VaultAdmin, then this method fails.

SOLIDWORKS Workgroup PDM 2004 FCS and later support changing configuration-specific properties using the SOLIDWORKS Workgroup PDM API.

## See Also

[IPDMWProperties Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties.html)
[IPDMWProperties Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
