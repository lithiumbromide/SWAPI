---
title: "Next Method (IEnumModelViews)"
project: "SOLIDWORKS API Help"
interface: "IEnumModelViews"
member: "Next"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews~Next.html"
---

# Next Method (IEnumModelViews)

Gets the next model view in the model views enumeration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As ModelView, _
   ByRef PceltFetched As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumModelViews
Dim Celt As System.Integer
Dim Rgelt As ModelView
Dim PceltFetched As System.Integer

instance.Next(Celt, Rgelt, PceltFetched)
```

### C#

```csharp
void Next(
   System.int Celt,
   out ModelView Rgelt,
   out System.int PceltFetched
)
```

### C++/CLI

```cpp
void Next(
   System.int Celt,
   [Out] ModelView^ Rgelt,
   [Out] System.int PceltFetched
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Celt`: Number of model views for the model views enumeration
- `Rgelt`: Pointer to an array of [model views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) of size Celt
- `PceltFetched`: Pointer to the number of model views returned from the list; this value can be less than celt if you ask for more model views than exist, or it can be NULL if no more model views exist

## VBA Syntax

See [EnumModelViews::Next](ms-its:sldworksapivb6.chm::/sldworks~EnumModelViews~Next.html).

## Remarks

For use in in-process DLLs only.

## See Also

[IEnumModelViews Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews.html)
[IEnumModelViews Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews_members.html)
