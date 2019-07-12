export default $(document).ready((e) => {
  $(function () {
    const $i18nAddresses = $('.i18n-address');
    $i18nAddresses.each(function () {
      const $form = $(this).closest('form');
      const $countryField = $form.find('select[name=country]');
      const $previewField = $form.find('input.preview');
      const $triggeredByCountryField = $form.find('input.triggered_by_country');
      $countryField.on('change', () => {
        $previewField.val('on');
        $triggeredByCountryField.val('on');
        $form.submit();
      });
    });
  });

  let $deleteAdressIcons = $('.icons');
  let $deleteAdressIcon = $('.delete-icon');
  let $deleteAddress = $('.address-delete');

  $deleteAdressIcon.on('click', (e) => {
    if ($deleteAddress.hasClass('none')) {
      $deleteAddress.removeClass('none');
      $deleteAdressIcons.addClass('none');
    } else {
      $deleteAddress.addClass('none');
    }
  });

  $deleteAddress.find('.cancel').on('click', (e) => {
    $deleteAddress.addClass('none');
    $deleteAdressIcons.removeClass('none');
  });

  // New address dropdown

  let $addressShow = $('.address_show label');
  let $addressHide = $('.address_hide label');
  let $addressForm = $('.checkout__new-address');
  let $initialValue = $('#address_new_address').prop('checked');

  $addressShow.click((e) => {
    if (shippingAddress === '') {
      $addressForm.slideDown('slow');
    }
  });
  $addressHide.click((e) => {
    $addressForm.slideUp('slow');
    if (shippingAddress) {
      $(this).find('input').prop('checked', true).trigger('change');
    }
  });

  $(document).on('change', 'input[type="radio"][name="address"]', function () {
    if (shippingAddress) {
      if ($(this).prop('checked')) {
        const $form = $(this).closest('form');
        if ($(this).prop('value') === 'new_address') {
          const $previewField = $form.find('input.preview');
          $previewField.val('on');
        }
        $form.submit();
      }
    }
  });

  if ($initialValue) {
    $addressForm.slideDown(0);
  } else {
    $addressForm.slideUp(0);
  }
  if (initialAddress) {
    $('.address_hide input[type="radio"][name="address"][value="' + initialAddress + '"').prop('checked', true);
  }
});
