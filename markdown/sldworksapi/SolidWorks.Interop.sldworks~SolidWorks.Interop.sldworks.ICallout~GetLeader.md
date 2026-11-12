---
title: "GetLeader Method (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "GetLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~GetLeader.html"
---

# GetLeader Method (ICallout)

Gets the leader properties of the callout.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeader( _
   ByRef Visible As System.Boolean, _
   ByRef Multiple As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim Visible As System.Boolean
Dim Multiple As System.Boolean
Dim value As System.Boolean

value = instance.GetLeader(Visible, Multiple)
```

### C#

```csharp
System.bool GetLeader(
   out System.bool Visible,
   out System.bool Multiple
)
```

### C++/CLI

```cpp
System.bool GetLeader(
   [Out] System.bool Visible,
   [Out] System.bool Multiple
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Visible`: True if leader is displayed, false if not (see **Remarks**)
- `Multiple`: True if multiple leaders are displayed, false if not

## VBA Syntax

See [Callout::GetLeader](ms-its:sldworksapivb6.chm::/sldworks~Callout~GetLeader.html).

## Remarks

If Visible is false, then [ICallout::TargetStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout~TargetStyle.html) is swCalloutTargetStyle_None.

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetLeader.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
