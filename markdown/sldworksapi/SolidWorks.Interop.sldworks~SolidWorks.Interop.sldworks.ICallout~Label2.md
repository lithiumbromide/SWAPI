---
title: "Label2 Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "Label2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Label2.html"
---

# Label2 Property (ICallout)

Gets or sets the text for the label in the specified row of this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property Label2( _
   ByVal RowID As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim RowID As System.Integer
Dim value As System.String

instance.Label2(RowID) = value

value = instance.Label2(RowID)
```

### C#

```csharp
System.string Label2(
   System.int RowID
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ Label2 {
   System.String^ get(System.int RowID);
   void set (System.int RowID, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowID`: Row for label

### Property Value

Text for label

## VBA Syntax

See [Callout::Label2](ms-its:sldworksapivb6.chm::/sldworks~Callout~Label2.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::SkipColon Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SkipColon.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
