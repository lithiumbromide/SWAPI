---
title: "DropTestStudyOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "DropTestStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestStudyOptions.html"
---

# DropTestStudyOptions Property (ICWStudy)

Gets the options for this drop test study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DropTestStudyOptions As CWDropTestStudyOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWDropTestStudyOptions

value = instance.DropTestStudyOptions
```

### C#

```csharp
CWDropTestStudyOptions DropTestStudyOptions {get;}
```

### C++/CLI

```cpp
property CWDropTestStudyOptions^ DropTestStudyOptions {
   CWDropTestStudyOptions^ get();
}
```

### Property Value

[ICWDropTestStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestStudyOptions.html)

## VBA Syntax

See [CWStudy::DropTestStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~DropTestStudyOptions.html).

## Examples

[Create Drop Test Study (VBA)](Create_Drop_Test_Study_Example_VB.htm)
[Create Drop Test Study (VB.NET)](Create_Drop_Test_Study_Example_VBNET.htm)
[Create Drop Test Study (C#)](Create_Drop_Test_Study_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::AddDropTestSetup Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~AddDropTestSetup.html)
[ICWStudy::DropTestResultOptions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestResultOptions.html)
[ICWStudy::DropTestSetup Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestSetup.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
