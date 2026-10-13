---
title: "Select3 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "Select3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select3.html"
---

# Select3 Method (IComponent2)

Obsolete. Superseded by [IComponent2::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Select4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select3( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select3(Append, Data)
```

### C#

```csharp
System.bool Select3(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select3(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the selection to the selection list, false replaces the selection list
- `Data`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the component is selected, false if not

## VBA Syntax

See [Component2::Select3](ms-its:sldworksapivb6.chm::/sldworks~Component2~Select3.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
