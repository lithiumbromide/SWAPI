---
title: "Value Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "Value"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Value.html"
---

# Value Property (ICallout)

Gets or sets the value in for the specified row in this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property Value( _
   ByVal RowID As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim RowID As System.Integer
Dim value As System.String

instance.Value(RowID) = value

value = instance.Value(RowID)
```

### C#

```csharp
System.string Value(
   System.int RowID
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ Value {
   System.String^ get(System.int RowID);
   void set (System.int RowID, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowID`: Row in callout

### Property Value

Value

## VBA Syntax

See [Callout::Value](ms-its:sldworksapivb6.chm::/sldworks~Callout~Value.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::ValueInactive Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~ValueInactive.html)
[ICallout::TextColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TextColor.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
