---
title: "GetUpdateStamp Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetUpdateStamp"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetUpdateStamp.html"
---

# GetUpdateStamp Method (IBody2)

Gets the update stamp for the body as of the last rebuild.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUpdateStamp() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Integer

value = instance.GetUpdateStamp()
```

### C#

```csharp
System.int GetUpdateStamp()
```

### C++/CLI

```cpp
System.int GetUpdateStamp();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Update stamp

## VBA Syntax

See [Body2::GetUpdateStamp](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetUpdateStamp.html).

## Remarks

The update stamp is not changed if the features contributing to the body geometry have not been rebuilt.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
