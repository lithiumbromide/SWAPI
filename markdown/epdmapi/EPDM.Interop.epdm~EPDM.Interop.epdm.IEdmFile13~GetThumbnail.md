---
title: "GetThumbnail Method (IEdmFile13)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile13"
member: "GetThumbnail"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13~GetThumbnail.html"
---

# GetThumbnail Method (IEdmFile13)

Obsolete. Superseded by [IEdmFile15::GetThumbnail2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile15~GetThumbnail2.html).

## Syntax

### Visual Basic

```vb
Function GetThumbnail() As System.Object
```

### C#

```csharp
System.object GetThumbnail()
```

### C++/CLI

```cpp
System.Object^ GetThumbnail();
```

### Return Value

IPicture

## Examples

'This code snippet demonstrates how to convert the IPicture object returned by this method to a usable bitmap.

VB.NET:

```
Imports stdole
Imports System
Imports System.Drawing
Imports System.Windows.Forms
```

```
Module Module1

    Sub Main()
```

```
       ...
```

```
       Dim objBitMap As Object = aFile.GetThumbnail
       Dim imgPreview As System.Drawing.Image = PictureDispConverter.Convert(objBitMap)
       imgPreview.Save(sExtractDir + sFilename + ".bmp", Drawing.Imaging.ImageFormat.Bmp)
       imgPreview.Dispose()

    End Sub

End Module

'Class1
Public Class PictureDispConverter

    Inherits System.Windows.Forms.AxHost

    Public Sub New()
        MyBase.New("GUID_format5_value")
    End Sub

    Public Shared Function Convert(ByVal objIDispImage As Object) As System.Drawing.Image
        Dim objPicture As System.Drawing.Image
        objPicture = CType(System.Windows.Forms.AxHost.GetPictureFromIPicture(objIDispImage), System.Drawing.Image)
        Return objPicture
    End Function

End Class
```

## Remarks

If a thumbnail of this file is not available, this method returns Nothing or null.

## See Also

[IEdmFile13 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13.html)
[IEdmFile13 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13_members.html)
[IEdmEnumeratorVariable5::GetThumbnail Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~GetThumbnail.html)

## Availability

SOLIDWORKS PDM Professional 2018
