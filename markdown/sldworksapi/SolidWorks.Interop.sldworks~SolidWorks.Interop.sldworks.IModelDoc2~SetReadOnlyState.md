---
title: "SetReadOnlyState Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetReadOnlyState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetReadOnlyState.html"
---

# SetReadOnlyState Method (IModelDoc2)

Sets whether this document is read-only or read-write.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetReadOnlyState( _
   ByVal SetReadOnly As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim SetReadOnly As System.Boolean
Dim value As System.Boolean

value = instance.SetReadOnlyState(SetReadOnly)
```

### C#

```csharp
System.bool SetReadOnlyState(
   System.bool SetReadOnly
)
```

### C++/CLI

```cpp
System.bool SetReadOnlyState(
   System.bool SetReadOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SetReadOnly`: True to set this document to be read-only, false to set this document to read-write

### Return Value

True if method executes successfully, false if not

## VBA Syntax

See [ModelDoc2::SetReadOnlyState](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetReadOnlyState.html).

## Remarks

If the file is opened as read-write, specifying read-only should work except if it is a new file that has not yet been saved.

If the file is opened as read-only in SOLIDWORKS, then specifying read-write only changes the internal SOLIDWORKS state (not the access rights on disk) and only succeeds if it would be possible to open this file with write access. If the file is read-only on disk or if another user has it open with write access, then this method does not change the internal state to writeable; the document remains read-only.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IsOpenedReadOnly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedReadOnly.html)
[IModelDoc2::IsOpenedViewOnly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedViewOnly.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
