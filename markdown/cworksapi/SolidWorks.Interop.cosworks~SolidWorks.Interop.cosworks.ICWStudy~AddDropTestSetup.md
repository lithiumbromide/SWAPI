---
title: "AddDropTestSetup Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "AddDropTestSetup"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~AddDropTestSetup.html"
---

# AddDropTestSetup Method (ICWStudy)

Adds a setup to this drop test study.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDropTestSetup( _
   ByVal EntityForGravity As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWDropTestSetup
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim EntityForGravity As System.Object
Dim ErrorCode As System.Integer
Dim value As CWDropTestSetup

value = instance.AddDropTestSetup(EntityForGravity, ErrorCode)
```

### C#

```csharp
CWDropTestSetup AddDropTestSetup(
   System.object EntityForGravity,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWDropTestSetup^ AddDropTestSetup(
   System.Object^ EntityForGravity,
   [Out] System.int ErrorCode
)
```

### Parameters

- `EntityForGravity`: Entity to drop
- `ErrorCode`: Status as defined by [swsDropTestSetUpError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDropTestSetUpError_e.html)

### Return Value

[ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html)

## VBA Syntax

See [CWStudy::AddDropTestSetup](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~AddDropTestSetup.html).

## Examples

[Create Drop Test Study (VBA)](Create_Drop_Test_Study_Example_VB.htm)
[Create Drop Test Study (VB.NET)](Create_Drop_Test_Study_Example_VBNET.htm)
[Create Drop Test Study (C#)](Create_Drop_Test_Study_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::DropTestResultOptions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestResultOptions.html)
[ICWStudy::DropTestSetup Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestSetup.html)
[ICWStudy::DropTestStudyOptions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestStudyOptions.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
