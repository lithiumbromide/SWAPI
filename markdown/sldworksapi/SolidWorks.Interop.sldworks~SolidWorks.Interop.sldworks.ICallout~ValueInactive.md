---
title: "ValueInactive Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "ValueInactive"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~ValueInactive.html"
---

# ValueInactive Property (ICallout)

Gets or sets whether the user can edit the value in the specified row in this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property ValueInactive( _
   ByVal RowID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim RowID As System.Integer
Dim value As System.Boolean

instance.ValueInactive(RowID) = value

value = instance.ValueInactive(RowID)
```

### C#

```csharp
System.bool ValueInactive(
   System.int RowID
) {get; set;}
```

### C++/CLI

```cpp
property System.bool ValueInactive {
   System.bool get(System.int RowID);
   void set (System.int RowID, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowID`: Row in callout

### Property Value

True if the value in this row cannot be modified, false if it can

## VBA Syntax

See [Callout::ValueInactive](ms-its:sldworksapivb6.chm::/sldworks~Callout~ValueInactive.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::Value Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Value.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
