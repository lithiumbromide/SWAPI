---
title: "Show Method (IManipulator)"
project: "SOLIDWORKS API Help"
interface: "IManipulator"
member: "Show"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Show.html"
---

# Show Method (IManipulator)

Shows the manipulator in this SOLIDWORKS part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Show( _
   ByVal PModelDoc As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IManipulator
Dim PModelDoc As System.Object

instance.Show(PModelDoc)
```

### C#

```csharp
void Show(
   System.object PModelDoc
)
```

### C++/CLI

```cpp
void Show(
   System.Object^ PModelDoc
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PModelDoc`: [Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [Manipulator::Show](ms-its:sldworksapivb6.chm::/sldworks~Manipulator~Show.html).

## Examples

[Create Triad Manipulator (VBA)](Create_Triad_Manipulator_Example_VB.htm)
[Create Triad Manipulator (VB.NET)](Create_Triad_Manipulator_Example_VBNET.htm)
[Create Triad Manipulator (C#)](Create_Triad_Manipulator_Example_CSharp.htm)

## See Also

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html)
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
