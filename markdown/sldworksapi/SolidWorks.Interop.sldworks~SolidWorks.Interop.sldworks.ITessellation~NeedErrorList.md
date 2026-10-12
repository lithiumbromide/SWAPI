---
title: "NeedErrorList Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "NeedErrorList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList.html"
---

# NeedErrorList Property (ITessellation)

Gets or sets the need error list option.

## Syntax

### Visual Basic (Declaration)

```vb
Property NeedErrorList As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Boolean

instance.NeedErrorList = value

value = instance.NeedErrorList
```

### C#

```csharp
System.bool NeedErrorList {get; set;}
```

### C++/CLI

```cpp
property System.bool NeedErrorList {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True generates need error list option, false to not

## VBA Syntax

See [Tessellation::NeedErrorList](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~NeedErrorList.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellate::GetErrorList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetErrorList.html)
[ITessellate::IGetErrorList2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.html)
[ITessellate::IGetErrorListCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorListCount.html)
