---
title: "AddFileOpenItem2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddFileOpenItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileOpenItem2.html"
---

# AddFileOpenItem2 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddFileOpenItem3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddFileOpenItem3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFileOpenItem2( _
   ByVal Cookie As System.Integer, _
   ByVal MethodName As System.String, _
   ByVal Description As System.String, _
   ByVal Extension As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim MethodName As System.String
Dim Description As System.String
Dim Extension As System.String
Dim value As System.Boolean

value = instance.AddFileOpenItem2(Cookie, MethodName, Description, Extension)
```

### C#

```csharp
System.bool AddFileOpenItem2(
   System.int Cookie,
   System.string MethodName,
   System.string Description,
   System.string Extension
)
```

### C++/CLI

```cpp
System.bool AddFileOpenItem2(
   System.int Cookie,
   System.String^ MethodName,
   System.String^ Description,
   System.String^ Extension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`:
- `MethodName`:
- `Description`:
- `Extension`:

## VBA Syntax

See [SldWorks::AddFileOpenItem2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddFileOpenItem2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
