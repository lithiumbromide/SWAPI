---
title: "AddToolbar3 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddToolbar3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar3.html"
---

# AddToolbar3 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddToolbar4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddToolbar4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddToolbar3( _
   ByVal Cookie As System.Integer, _
   ByVal Title As System.String, _
   ByVal SmallBitmapResourceID As System.Integer, _
   ByVal LargeBitmapResourceID As System.Integer, _
   ByVal MenuPositionForToolbar As System.Integer, _
   ByVal DocumentType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim Title As System.String
Dim SmallBitmapResourceID As System.Integer
Dim LargeBitmapResourceID As System.Integer
Dim MenuPositionForToolbar As System.Integer
Dim DocumentType As System.Integer
Dim value As System.Integer

value = instance.AddToolbar3(Cookie, Title, SmallBitmapResourceID, LargeBitmapResourceID, MenuPositionForToolbar, DocumentType)
```

### C#

```csharp
System.int AddToolbar3(
   System.int Cookie,
   System.string Title,
   System.int SmallBitmapResourceID,
   System.int LargeBitmapResourceID,
   System.int MenuPositionForToolbar,
   System.int DocumentType
)
```

### C++/CLI

```cpp
System.int AddToolbar3(
   System.int Cookie,
   System.String^ Title,
   System.int SmallBitmapResourceID,
   System.int LargeBitmapResourceID,
   System.int MenuPositionForToolbar,
   System.int DocumentType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`:
- `Title`:
- `SmallBitmapResourceID`:
- `LargeBitmapResourceID`:
- `MenuPositionForToolbar`:
- `DocumentType`:

## VBA Syntax

See [SldWorks::AddToolbar3](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddToolbar3.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
