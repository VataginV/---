from django import forms
from .models import Tos, District, SubDistrict

class TosAdminForm(forms.ModelForm):
    class Meta:
        model = Tos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['subdistrict'].queryset = SubDistrict.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Неверный ввод от клиента; игнорируем и возвращаем пустой queryset подрайонов
        elif self.instance.pk:
            self.fields['subdistrict'].queryset = self.instance.district.subdistricts.order_by('name')
        else:
            self.fields['subdistrict'].queryset = SubDistrict.objects.none()