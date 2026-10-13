---
title: "LoadFromFile Method (IPDMWSearchCriteria)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchCriteria"
member: "LoadFromFile"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~LoadFromFile.html"
---

# LoadFromFile Method (IPDMWSearchCriteria)

Clears the current search criteria and loads the search criteria from the specified file (.sqy).

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadFromFile( _
   ByVal filename As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchCriteria
Dim filename As System.String
Dim value As System.Boolean

value = instance.LoadFromFile(filename)
```

### C#

```csharp
System.bool LoadFromFile(
   System.string filename
)
```

### C++/CLI

```cpp
System.bool LoadFromFile(
   System.String^ filename
)
```

### Parameters

- `filename`: Path and filename of file containing search criteria

### Return Value

True if search criteria is loaded from the specified file, false if not

## VBA Syntax

See [PDMWSearchCriteria::LoadFromFile](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchCriteria~LoadFromFile.html).

## Examples

[Create Search Criteria and Search Vault (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## See Also

[IPDMWSearchCriteria Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria.html)
[IPDMWSearchCriteria Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria_members.html)
[IPDMWSearchCriteria::AddCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~AddCriteria.html)
[IPDMWSearchCriteria::GetCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~GetCriteria.html)
[IPDMWSearchCriteria::RemoveCriteria Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~RemoveCriteria.html)
[IPDMWSearchCriteria::SaveToFile Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchCriteria~SaveToFile.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
