---
title: "StudyManager Property (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "StudyManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~StudyManager.html"
---

# StudyManager Property (ICWModelDoc)

Gets the study manager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StudyManager As CWStudyManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim value As CWStudyManager

value = instance.StudyManager
```

### C#

```csharp
CWStudyManager StudyManager {get;}
```

### C++/CLI

```cpp
property CWStudyManager^ StudyManager {
   CWStudyManager^ get();
}
```

### Property Value

[Study manager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyManager.html)

## VBA Syntax

See [CWModelDoc::StudyManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~StudyManager.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
