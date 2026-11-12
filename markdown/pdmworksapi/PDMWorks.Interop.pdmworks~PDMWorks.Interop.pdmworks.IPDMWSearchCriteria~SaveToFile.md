---
title: "SaveToFile Method (IPDMWSearchCriteria)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchCriteria"
member: "SaveToFile"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~SaveToFile.html"
---

# SaveToFile Method (IPDMWSearchCriteria)

Saves the search criteria to the specified file (.sqy).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveToFile( _
   ByVal filename As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchCriteria
Dim filename As System.String
Dim value As System.Boolean

value = instance.SaveToFile(filename)
```

### C#

```csharp
System.bool SaveToFile(
   System.string filename
)
```

### C++/CLI

```cpp
System.bool SaveToFile(
   System.String^ filename
)
```

### Parameters

- `filename`: Path and filename of the file to which to save the search criteria

### Return Value

True if the search criteria is saved to the specified file, false if not

## VBA Syntax

See [PDMWSearchCriteria::SaveToFile](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchCriteria~SaveToFile.html).

## Examples

[Create Search Criteria and Search Vault (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## See Also

[IPDMWSearchCriteria Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria.html)
[IPDMWSearchCriteria Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria_members.html)
[IPDMWSearchCriteria::LoadFromFile Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~LoadFromFile.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
