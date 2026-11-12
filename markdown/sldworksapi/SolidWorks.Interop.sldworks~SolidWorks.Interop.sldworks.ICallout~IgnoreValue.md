---
title: "IgnoreValue Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "IgnoreValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~IgnoreValue.html"
---

# IgnoreValue Property (ICallout)

Gets or sets whether to ignore the callout value in the given row.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreValue( _
   ByVal RowID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim RowID As System.Integer
Dim value As System.Boolean

instance.IgnoreValue(RowID) = value

value = instance.IgnoreValue(RowID)
```

### C#

```csharp
System.bool IgnoreValue(
   System.int RowID
) {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreValue {
   System.bool get(System.int RowID);
   void set (System.int RowID, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowID`: Index of callout row

### Property Value

True to ignore callout value, false to not

## VBA Syntax

See [Callout::IgnoreValue](ms-its:sldworksapivb6.chm::/sldworks~Callout~IgnoreValue.html).

## Examples

[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

## Remarks

Use this API to remove the white space that remains in the callout when [ICallout::Value](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout~Value.html) is set to an empty string.

This property applies only to a callout that is independent of a selection or created with [IModelDocExtension::CreateCallout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateCallout.html).

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
