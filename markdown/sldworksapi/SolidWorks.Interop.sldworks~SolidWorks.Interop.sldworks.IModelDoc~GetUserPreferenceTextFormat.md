---
title: "GetUserPreferenceTextFormat Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetUserPreferenceTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetUserPreferenceTextFormat.html"
---

# GetUserPreferenceTextFormat Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetUserPreferenceTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUserPreferenceTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim value As System.Object

value = instance.GetUserPreferenceTextFormat(UserPreferenceValue)
```

### C#

```csharp
System.object GetUserPreferenceTextFormat(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
System.Object^ GetUserPreferenceTextFormat(
   System.int UserPreferenceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`:

## VBA Syntax

See [ModelDoc::GetUserPreferenceTextFormat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetUserPreferenceTextFormat.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
