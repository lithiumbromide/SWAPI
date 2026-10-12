---
title: "GetLastErrorCode Method (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "GetLastErrorCode"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~GetLastErrorCode.html"
---

# GetLastErrorCode Method (ICWLinkageRod)

Gets the last error thrown for this linkage rod connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLastErrorCode() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod
Dim value As System.Integer

value = instance.GetLastErrorCode()
```

### C#

```csharp
System.int GetLastErrorCode()
```

### C++/CLI

```cpp
System.int GetLastErrorCode();
```

### Return Value

Error code as defined by [swsLinkageRodEndEditErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinkageRodEndEditErrors_e.html)

## VBA Syntax

See [CWLinkageRod::GetLastErrorCode](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~GetLastErrorCode.html).

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
