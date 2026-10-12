---
title: "LoadCaseManager Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "LoadCaseManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~LoadCaseManager.html"
---

# LoadCaseManager Property (ICWStudy)

Gets the Load Case Manager for this static study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LoadCaseManager As CWLoadCaseManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWLoadCaseManager

value = instance.LoadCaseManager
```

### C#

```csharp
CWLoadCaseManager LoadCaseManager {get;}
```

### C++/CLI

```cpp
property CWLoadCaseManager^ LoadCaseManager {
   CWLoadCaseManager^ get();
}
```

### Property Value

[ICWLoadCaseManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)

## VBA Syntax

See [CWStudy::LoadCaseManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~LoadCaseManager.html).

## Examples

[Access Load Case Manager (VBA)](Access_Load_Case_Manager_Example_VB.htm)
[Access Load Case Manager (VB.NET)](Access_Load_Case_Manager_Example_VBNET.htm)
[Access Load Case Manager (C#)](Access_Load_Case_Manager_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
