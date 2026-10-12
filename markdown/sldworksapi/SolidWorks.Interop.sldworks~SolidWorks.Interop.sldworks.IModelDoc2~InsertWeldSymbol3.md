---
title: "InsertWeldSymbol3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertWeldSymbol3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertWeldSymbol3.html"
---

# InsertWeldSymbol3 Method (IModelDoc2)

Inserts a weld symbol into the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertWeldSymbol3() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.InsertWeldSymbol3()
```

### C#

```csharp
System.object InsertWeldSymbol3()
```

### C++/CLI

```cpp
System.Object^ InsertWeldSymbol3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Newly created [weld symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html)

## VBA Syntax

See [ModelDoc2::InsertWeldSymbol3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertWeldSymbol3.html).

## Examples

[Insert Weld Symbol Example (VBA)](Insert_Weld_Symbol_Example_VB.htm)
[Insert Weld Symbol Example (VB.NET)](Insert_Weld_Symbol_Example_VBNET.htm)
[Insert Weld Symbol Example (C#)](Insert_Weld_Symbol_Example_CSharp.htm)

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

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
