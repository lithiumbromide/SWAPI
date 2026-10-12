---
title: "SetLeader Method (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "SetLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetLeader.html"
---

# SetLeader Method (ICallout)

Sets the leader properties of the callout.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLeader( _
   ByVal Visible As System.Boolean, _
   ByVal Multiple As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim Visible As System.Boolean
Dim Multiple As System.Boolean
Dim value As System.Boolean

value = instance.SetLeader(Visible, Multiple)
```

### C#

```csharp
System.bool SetLeader(
   System.bool Visible,
   System.bool Multiple
)
```

### C++/CLI

```cpp
System.bool SetLeader(
   System.bool Visible,
   System.bool Multiple
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Visible`: True to display the leader, false to not (see **Remarks**)
- `Multiple`: True to display multiple leaders, false to not

### Return Value

True if the operation is successful, false if not

## VBA Syntax

See [Callout::SetLeader](ms-its:sldworksapivb6.chm::/sldworks~Callout~SetLeader.html).

## Examples

[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

## Remarks

You can only use this method before the callout is shown or while the callout is hidden.

If Visible is set to false, then [ICallout::TargetStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout~TargetStyle.html) is automatically set to swCalloutTargetStyle_None.

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::GetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~GetLeader.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
