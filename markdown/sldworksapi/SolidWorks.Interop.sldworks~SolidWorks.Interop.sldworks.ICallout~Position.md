---
title: "Position Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "Position"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Position.html"
---

# Position Property (ICallout)

Gets and sets the position of this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property Position As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim value As MathPoint

instance.Position = value

value = instance.Position
```

### C#

```csharp
MathPoint Position {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ Position {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Position](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of this callout

## VBA Syntax

See [Callout::Position](ms-its:sldworksapivb6.chm::/sldworks~Callout~Position.html).

## Examples

[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::GetTargetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~GetTargetPoint.html)
[ICallout::SetTargetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetTargetPoint.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
