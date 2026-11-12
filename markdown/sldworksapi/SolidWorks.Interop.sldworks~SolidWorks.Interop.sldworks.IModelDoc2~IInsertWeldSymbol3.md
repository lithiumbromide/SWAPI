---
title: "IInsertWeldSymbol3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IInsertWeldSymbol3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertWeldSymbol3.html"
---

# IInsertWeldSymbol3 Method (IModelDoc2)

Inserts a weld symbol into the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertWeldSymbol3() As WeldSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As WeldSymbol

value = instance.IInsertWeldSymbol3()
```

### C#

```csharp
WeldSymbol IInsertWeldSymbol3()
```

### C++/CLI

```cpp
WeldSymbol^ IInsertWeldSymbol3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Newly created [weld symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html)

## VBA Syntax

See [ModelDoc2::IInsertWeldSymbol3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IInsertWeldSymbol3.html).

## Remarks

To use this method, insert the weld symbol into the model and then manipulate the properties and methods on the [IWeldSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html) object.

A list of weld symbol names can be found in **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english\gtol.sym****.** The currently supported list of ISO weld symbols is:

- BUTT
- BUSQ
- BUSV
- BUSB
- BUSVBR
- BUSBR
- BUSU
- BUSJ
- BACK
- FILL
- PLUG
- SPOT
- SEAM
- SEAMC
- JSPT
- JSM

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertWeldSymbol3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertWeldSymbol3.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
